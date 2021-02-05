rule _PowerBASICCC_3_0x_qtxnsi
{
	meta:
		description = "PowerBASICCC 3_0x"
	strings:
		$a = {558BEC535657BB00????00662EF705??????0004000F85}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
