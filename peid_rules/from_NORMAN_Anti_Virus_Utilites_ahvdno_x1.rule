rule _from_NORMAN_Anti_Virus_Utilites_ahvdno
{
	meta:
		description = "from NORMAN Anti_Virus Utilites"
	strings:
		$a = {E8????5B52452F4E4444535D0D0A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
