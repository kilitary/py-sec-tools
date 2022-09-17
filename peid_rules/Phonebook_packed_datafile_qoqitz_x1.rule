rule _Phonebook_packed_datafile_qoqitz
{
	meta:
		description = "Phonebook packed datafile"
	strings:
		$a = {215048325041434B24}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
