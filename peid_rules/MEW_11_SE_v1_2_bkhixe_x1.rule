rule _MEW_11_SE_v1_2_bkhixe
{
	meta:
		description = "MEW 11 SE v1_2"
	strings:
		$a = {E9??????FF0C????000000000000000000??????000C????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
