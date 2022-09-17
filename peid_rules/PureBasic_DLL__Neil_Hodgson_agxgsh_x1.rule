rule _PureBasic_DLL__Neil_Hodgson_agxgsh
{
	meta:
		description = "PureBasic DLL __ Neil Hodgson"
	strings:
		$a = {837C24080175??8B442404A3??????10E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
