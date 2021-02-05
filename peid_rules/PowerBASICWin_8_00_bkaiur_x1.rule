rule _PowerBASICWin_8_00_bkaiur
{
	meta:
		description = "PowerBASICWin 8_00"
	strings:
		$a = {558BEC535657BB00????00662EF705????400004007505E914040000E91902}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
