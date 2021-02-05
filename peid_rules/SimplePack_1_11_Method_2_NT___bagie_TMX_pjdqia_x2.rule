rule _SimplePack_1_11_Method_2_NT___bagie_TMX_pjdqia
{
	meta:
		description = "SimplePack 1_11 Method 2_NT_ __ bagie_TMX"
	strings:
		$a = {4D5A90EB010052E989010000504500004C010200000000000000000000000000E0000F030B01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
