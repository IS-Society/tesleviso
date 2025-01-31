FROM odoo:17.0

# Set working directory
WORKDIR /usr/lib/python3/dist-packages/odoo

# Copy konfigurasi dan addons ke dalam container
COPY conf/odoo.conf /etc/odoo/odoo.conf
COPY addons /mnt/extra-addons

# Jalankan Odoo dengan konfigurasi yang telah disiapkan
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]
