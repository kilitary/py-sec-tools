rule _EZIP_v1_0_pxiyez
{
	meta:
		description = "EZIP v1_0"
	strings:
		$a = {E919320000E97C2A0000E919240000E9FF230000E91E2E0000E9882E0000E92C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
