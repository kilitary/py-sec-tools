rule _Obsidium_1_2_5_0__Obsidium_Software_gbumhd
{
	meta:
		description = "Obsidium 1_2_5_0 __ Obsidium Software"
	strings:
		$a = {E80E0000008B54240C8382B8000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
