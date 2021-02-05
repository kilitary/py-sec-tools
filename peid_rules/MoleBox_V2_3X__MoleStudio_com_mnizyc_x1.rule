rule _MoleBox_V2_3X__MoleStudio_com_mnizyc
{
	meta:
		description = "MoleBox V2_3X __ MoleStudio_com"
	strings:
		$a = {E80000000060E84F000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
