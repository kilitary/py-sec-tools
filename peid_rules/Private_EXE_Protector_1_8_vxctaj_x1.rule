rule _Private_EXE_Protector_1_8_vxctaj
{
	meta:
		description = "Private EXE Protector 1_8"
	strings:
		$a = {BBDCEE0D76D9D08D1685D890D9D0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
