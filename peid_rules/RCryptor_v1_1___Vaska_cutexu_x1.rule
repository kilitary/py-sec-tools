rule _RCryptor_v1_1___Vaska_cutexu
{
	meta:
		description = "RCryptor v1_1 ___ Vaska"
	strings:
		$a = {8B042483E84F68????????FFD0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
