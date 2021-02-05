rule _Obsidium_V1_3_0_0__Obsidium_Software_lcrpvv
{
	meta:
		description = "Obsidium V1_3_0_0 __ Obsidium Software"
	strings:
		$a = {EB04????????E829000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
