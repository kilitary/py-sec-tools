rule _PE_Diminisher_v0_1_srzpav
{
	meta:
		description = "PE Diminisher v0_1"
	strings:
		$a = {5D8BC581EDB22C40002B85943E40002D710200008985983E40000FB6B59C3E40008BFD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
