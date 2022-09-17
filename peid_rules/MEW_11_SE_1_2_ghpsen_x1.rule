rule _MEW_11_SE_1_2_ghpsen
{
	meta:
		description = "MEW 11 SE 1_2"
	strings:
		$a = {E9????????0C??????0000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
