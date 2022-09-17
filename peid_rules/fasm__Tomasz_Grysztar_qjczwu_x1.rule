rule _fasm__Tomasz_Grysztar_qjczwu
{
	meta:
		description = "fasm __ Tomasz Grysztar"
	strings:
		$a = {6A24}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
