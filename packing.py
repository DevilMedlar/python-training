stickers = 26
pack_size = 4
full_packs = stickers // pack_size
leftover_stickers = stickers % pack_size
packed_stickers = stickers - leftover_stickers
division_result = stickers / pack_size
print(leftover_stickers)
print(packed_stickers)
print(full_packs)
print(division_result)
