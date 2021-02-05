rule _Obsidium_1_3_0_0__Obsidium_Software_ardzka
{
	meta:
		description = "Obsidium 1_3_0_0 __ Obsidium Software"
	strings:
		$a = {EB02????E825000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
