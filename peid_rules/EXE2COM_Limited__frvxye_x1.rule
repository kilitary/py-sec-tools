rule _EXE2COM_Limited__frvxye
{
	meta:
		description = "EXE2COM _Limited_"
	strings:
		$a = {BE????8B043D????74??BA????B409CD21CD20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
