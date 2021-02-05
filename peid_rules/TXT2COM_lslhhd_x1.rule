rule _TXT2COM_lslhhd
{
	meta:
		description = "TXT2COM"
	strings:
		$a = {E8????CD20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
