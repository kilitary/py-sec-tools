rule _Obsidium_v1_1_1_1_smmndz
{
	meta:
		description = "Obsidium v1_1_1_1"
	strings:
		$a = {EB02????E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
