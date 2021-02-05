rule _Vx_VCL_encrypted__jrhqqh
{
	meta:
		description = "Vx_ VCL _encrypted_"
	strings:
		$a = {01B9????8134????4646E2F8C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
