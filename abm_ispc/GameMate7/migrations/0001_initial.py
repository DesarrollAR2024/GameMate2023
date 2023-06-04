# Generated by Django 4.2.1 on 2023-06-04 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('informacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categoria de productos',
                'verbose_name_plural': 'categorias',
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('telefono', models.BigIntegerField()),
                ('nickname', models.CharField(max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'datos de los clientes',
                'verbose_name_plural': 'clientes',
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id_envio', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_envio', models.DateField()),
                ('localidad', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('cod_post', models.IntegerField()),
                ('estado_envio', models.CharField(max_length=20)),
                ('direccion_envio', models.CharField(max_length=30)),
                ('metodo_envio', models.CharField(max_length=30)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.cliente')),
            ],
            options={
                'verbose_name': 'informacion de envio',
                'verbose_name_plural': 'envios',
                'db_table': 'envio',
            },
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('numero_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('metodo_pago', models.CharField(max_length=20)),
                ('costo_envio', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fecha_factura', models.DateField()),
                ('fecha_pago', models.DateField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estado_pago', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'informacion de Facturacion',
                'verbose_name_plural': 'Facturaciones',
                'db_table': 'Facturacion',
            },
        ),
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id_juego', models.IntegerField(primary_key=True, serialize=False)),
                ('juego', models.CharField(max_length=30)),
                ('imagen', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Juegos',
                'verbose_name_plural': 'Juegos',
                'db_table': 'Juegos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('cuil', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'datos del proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id_redes', models.AutoField(primary_key=True, serialize=False)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('youtube', models.CharField(max_length=100, null=True)),
                ('tik_tok', models.CharField(max_length=100, null=True)),
                ('twitter', models.CharField(max_length=100, null=True)),
                ('twitch', models.CharField(max_length=100, null=True)),
                ('discord', models.CharField(max_length=100, null=True)),
                ('Usuarios', models.CharField(max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Redes socialesr',
                'verbose_name_plural': 'Redes',
                'db_table': 'Redes',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('nickname', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nac', models.DateField()),
                ('provincia', models.CharField(max_length=15)),
                ('disp_horaria', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=25)),
                ('contraseña', models.CharField(max_length=10)),
                ('imagen_perfil', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'datos de los usuarios',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.categoria')),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.proveedor')),
            ],
            options={
                'verbose_name': 'datos del producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField()),
                ('estado_pedido', models.CharField(max_length=20)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.cliente')),
                ('Envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.envio')),
                ('Facturacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.facturacion')),
            ],
            options={
                'verbose_name': 'datos del pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cantidad_pedido', models.IntegerField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.cliente')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.producto')),
            ],
            options={
                'verbose_name': 'datos de la orden',
                'verbose_name_plural': 'Ordenes',
                'db_table': 'Orden',
            },
        ),
        migrations.CreateModel(
            name='Jugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_jugador', models.CharField(max_length=15)),
                ('Juegos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.juegos')),
                ('Usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.usuarios')),
            ],
            options={
                'verbose_name': 'Jugar',
                'verbose_name_plural': 'Jugaremos',
                'db_table': 'Jugar',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id_galeria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_foto', models.CharField(max_length=25, null=True)),
                ('foto', models.CharField(max_length=50, null=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.usuarios')),
            ],
            options={
                'verbose_name': 'galeria de fotos',
                'verbose_name_plural': 'Galerias',
                'db_table': 'Galeria',
            },
        ),
        migrations.AddField(
            model_name='facturacion',
            name='Orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.orden'),
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id_dispositivos', models.IntegerField(primary_key=True, serialize=False)),
                ('pc', models.CharField(max_length=15, null=True)),
                ('version_celular', models.CharField(max_length=15, null=True)),
                ('nintendo_switch', models.CharField(max_length=10, null=True)),
                ('version_playstation', models.CharField(max_length=10, null=True)),
                ('version_xbox', models.CharField(max_length=10, null=True)),
                ('Usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.usuarios')),
            ],
            options={
                'verbose_name': 'dispositivos',
                'verbose_name_plural': 'dispositivos',
                'db_table': 'dispositivos',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=30)),
                ('cod_post', models.IntegerField()),
                ('provincia', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=50)),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.proveedor')),
            ],
            options={
                'verbose_name': 'todas las direcciones',
                'verbose_name_plural': 'direcciones',
                'db_table': 'direccion',
            },
        ),
        migrations.CreateModel(
            name='Compatibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dispositivos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.dispositivos')),
                ('Juegos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMate7.juegos')),
            ],
            options={
                'verbose_name': 'compatibilidad',
                'verbose_name_plural': 'compatibilidades',
                'db_table': 'compatibilidad',
            },
        ),
    ]
