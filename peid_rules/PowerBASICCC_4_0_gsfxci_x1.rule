rule _PowerBASICCC_4_0_gsfxci
{
	meta:
		description = "PowerBASICCC 4_0"
	strings:
		$a = {558BEC535657BB00??4000662EF705????400004007505E968050000E96E03}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
