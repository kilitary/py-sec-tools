rule _Obsidium_V1_2__Obsidium_Software_gunmcy
{
	meta:
		description = "Obsidium V1_2 __ Obsidium Software"
	strings:
		$a = {EB02????E8771E0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
