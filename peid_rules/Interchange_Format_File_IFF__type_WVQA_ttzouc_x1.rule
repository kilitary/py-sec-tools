rule _Interchange_Format_File_IFF__type_WVQA_ttzouc
{
	meta:
		description = "Interchange Format File _IFF__ type WVQA"
	strings:
		$a = {464F524D????????5756514156514844}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
