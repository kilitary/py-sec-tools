rule _Obsidium_V1_2_5_8_V1_3_3_X__Obsidium_Software_kzwggl
{
	meta:
		description = "Obsidium V1_2_5_8_V1_3_3_X __ Obsidium Software"
	strings:
		$a = {EB01??E8??000000EB02????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
