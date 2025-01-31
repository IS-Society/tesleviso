FROM odoo:17.0

# Salin konfigurasi Odoo
COPY conf/odoo.conf /etc/odoo/odoo.conf

# Set direktori kerja
WORKDIR /var/lib/odoo

# Jalankan Odoo
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]
