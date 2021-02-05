rule _KByS_Packer_v0_28_yfpgbt
{
	meta:
		description = "KByS Packer v0_28"
	strings:
		$a = {68??????00E801000000C3C3608B7424248B7C2428FCB28033DBA4B302E86D00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
