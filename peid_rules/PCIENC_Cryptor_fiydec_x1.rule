rule _PCIENC_Cryptor_fiydec
{
	meta:
		description = "PCIENC Cryptor"
	strings:
		$a = {06504349454E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
