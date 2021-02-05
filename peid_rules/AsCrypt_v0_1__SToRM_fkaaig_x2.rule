rule _AsCrypt_v0_1__SToRM_fkaaig
{
	meta:
		description = "AsCrypt v0_1 __ SToRM"
	strings:
		$a = {83????E2????E2??FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
