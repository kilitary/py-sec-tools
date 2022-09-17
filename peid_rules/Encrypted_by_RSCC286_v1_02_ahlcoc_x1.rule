rule _Encrypted_by_RSCC286_v1_02_ahlcoc
{
	meta:
		description = "Encrypted by_ RSCC286 v1_02"
	strings:
		$a = {FE525343432F312E3032FE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
