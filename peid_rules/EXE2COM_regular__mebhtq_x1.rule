rule _EXE2COM_regular__mebhtq
{
	meta:
		description = "EXE2COM _regular_"
	strings:
		$a = {E98CCA81C3????3B16????76??BA????B409CD21CD200D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
