rule _PEncrypt_v3_0_gylras
{
	meta:
		description = "PEncrypt v3_0"
	strings:
		$a = {E8000000005D81ED051040008DB5241040008BFEB90F000000BB????????AD33C3E2FA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
