const mp = new MercadoPago('TEST-4509fe18-979c-4a38-8851-870aec28198f', {
  locale: 'es'
});
const bricksBuilder = mp.bricks();
const renderCardPaymentBrick = async (bricksBuilder) => {
  const settings = {
    initialization: {
      amount: 100, // monto a ser pago
      payer: {
        email: "",
      },
    },
    customization: {
      visual: {
        style: {
          theme: 'bootstrap', // | 'dark' | 'bootstrap' | 'flat'
        }
      },
    },
    callbacks: {
      onReady: () => {
        // callback llamado cuando Brick esté listo
      },
      onSubmit: (cardFormData) => {
        //  callback llamado cuando el usuario haga clic en el botón enviar los datos
        //  ejemplo de envío de los datos recolectados por el Brick a su servidor
        return new Promise((resolve, reject) => {
          fetch("/process_payment", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(cardFormData)
          })
            .then((response) => {
              // recibir el resultado del pago
              resolve();
            })
            .catch((error) => {
              // tratar respuesta de error al intentar crear el pago
              reject();
            })
        });
      },
      onError: (error) => {
        // callback llamado para todos los casos de error de Brick
      },
    },
  };
  window.cardPaymentBrickController = await bricksBuilder.create('cardPayment', 'cardPaymentBrick_container', settings);
};
renderCardPaymentBrick(bricksBuilder);