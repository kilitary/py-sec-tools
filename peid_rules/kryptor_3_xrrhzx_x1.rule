rule _kryptor_3_xrrhzx
{
	meta:
		description = "kryptor 3"
	strings:
		$a = {EB6687DB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
