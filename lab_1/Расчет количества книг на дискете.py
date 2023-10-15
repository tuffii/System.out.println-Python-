# TODO Найдите количество книг, которое можно разместить на дискете

disk_storage = 1.44
bite_mb = 1024
symbol_data = 4
symbol_count = 25
lines_count = 50
pages_count = 100

storage = disk_storage * bite_mb * bite_mb
book = symbol_data * symbol_count * lines_count * pages_count
print("Количество книг, помещающихся на дискету:", "{:.0f}".format(storage / book))
