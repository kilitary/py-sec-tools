rule _DalKrypt_1_0__by_DalKiT_edbffs
{
	meta:
		description = "DalKrypt 1_0 _ by DalKiT"
	strings:
		$a = {68001040005868??????005F33DBEB0D8A140380EA0780F2048814034381FB??????0072EBFFE7}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
