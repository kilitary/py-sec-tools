rule _CrunchPE_v3_0_x_x_tnrwzi
{
	meta:
		description = "CrunchPE v3_0_x_x"
	strings:
		$a = {03D6B440CD21B8024233D233C9CD218BD6B97801}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
