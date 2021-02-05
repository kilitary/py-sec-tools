rule _Dev_C__v4_ldovos
{
	meta:
		description = "Dev_C__ v4"
	strings:
		$a = {5589E583EC0883C4F46A??A1??????00FFD0E8??FFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
