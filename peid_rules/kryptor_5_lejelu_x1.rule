rule _kryptor_5_lejelu
{
	meta:
		description = "kryptor 5"
	strings:
		$a = {E803??????E9EB685833D27402E9E940427502}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
