rule _COOLcryptor_0_9__kongfoo_rwgvmx
{
	meta:
		description = "COOLcryptor 0_9 __ kongfoo"
	strings:
		$a = {E803000000E9EB07FF0424EB01FFC3E803000000EB02EAC3EB088D8D7208}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
