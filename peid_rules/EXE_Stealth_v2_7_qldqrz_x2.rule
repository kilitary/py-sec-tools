rule _EXE_Stealth_v2_7_qldqrz
{
	meta:
		description = "EXE Stealth v2_7"
	strings:
		$a = {EB0060EB00E8000000005D81EDD32640}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
