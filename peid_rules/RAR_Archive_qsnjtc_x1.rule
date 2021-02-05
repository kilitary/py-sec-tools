rule _RAR_Archive_qsnjtc
{
	meta:
		description = "RAR Archive"
	strings:
		$a = {52617221}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
