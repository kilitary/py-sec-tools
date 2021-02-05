rule _PE_Crypter_dzhqpq
{
	meta:
		description = "PE_Crypter"
	strings:
		$a = {60E8000000005DB9????????8031154181F9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
