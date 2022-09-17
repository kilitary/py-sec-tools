rule _LameCrypt__LaZaRus_irvhbl
{
	meta:
		description = "LameCrypt __ LaZaRus"
	strings:
		$a = {60669CBB00????0080B300104000904B83FBFF75F3669D61B8????4000FFE0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
