rule _kryptor_8_vosidg
{
	meta:
		description = "kryptor 8"
	strings:
		$a = {EB6A87DB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
