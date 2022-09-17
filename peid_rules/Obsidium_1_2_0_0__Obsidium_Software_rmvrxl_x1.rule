rule _Obsidium_1_2_0_0__Obsidium_Software_rmvrxl
{
	meta:
		description = "Obsidium 1_2_0_0 __ Obsidium Software"
	strings:
		$a = {EB02????E83F1E0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
