rule _CorelDraw_CMX_Graphics_format_uxgisp
{
	meta:
		description = "CorelDraw CMX Graphics format"
	strings:
		$a = {52494646????????434D5831}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
