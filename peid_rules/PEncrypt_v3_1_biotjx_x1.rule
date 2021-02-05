rule _PEncrypt_v3_1_biotjx
{
	meta:
		description = "PEncrypt v3_1"
	strings:
		$a = {E9??????00F00FC6}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
