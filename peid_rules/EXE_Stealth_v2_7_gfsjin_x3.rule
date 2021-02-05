rule _EXE_Stealth_v2_7_gfsjin
{
	meta:
		description = "EXE Stealth v2_7"
	strings:
		$a = {EB00EB2F536861726577617265202D20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
