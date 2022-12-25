import PySimpleGUI as sg
from zipper_backend import extract_archive, compress_files
import zipfile

sg.theme('DarkGreen6')

# COMPRESSOR
label1_c = sg.Text('.zip Compressor')
label2_c = sg.Text('Select file(s):')
input1_c = sg.Input(key='input1_c')
choose_button1_c = sg.FilesBrowse('Choose', key='tocompress')

label3_c = sg.Text('Select destination dir:')
input2_c = sg.Input(key='input2_c')
choose_button2_c = sg.FolderBrowse('Choose', key='folder_c')

compress_button = sg.Button('Compress')
output_label_c = sg.Text(key='output_c')
# EXTRACTOR
label1_e = sg.Text('.zip Extractor')
label2_e = sg.Text('Select archive:')
input1_e = sg.Input(key='input1_e')
choose_button1_e = sg.FileBrowse('Choose', key='toextract')

label3_e = sg.Text('Select destination dir:')
input2_e = sg.Input(key='input2_e')
choose_button2_e = sg.FolderBrowse('Choose', key='folder_e')

extract_button = sg.Button('Extract')
output_label_e = sg.Text(key='output_e')
#

window = sg.Window('Archive Extractor/Compressor',
                   layout=[[label1_c], [label2_c, input1_c, choose_button1_c],
                           [label3_c, input2_c, choose_button2_c],
                           [compress_button, output_label_c],
                           [label1_e], [label2_e, input1_e, choose_button1_e],
                           [label3_e, input2_e, choose_button2_e],
                           [extract_button, output_label_e]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()

    match event:
        case 'Extract':
            extract_path = values['toextract']
            dest_dir_e = values['folder_e']
            try:
                extract_archive(extract_path, dest_dir_e)
                window['output_e'].update(value='Extraction completed!')
                window['input2_c'].update(value='')
                window['input1_c'].update(value='')
            except zipfile.BadZipFile: sg.popup('Extension of archive to extract is not supported', font=('Helvetica', 14))
        case 'Compress':
            compress_path = values['tocompress'].split(';')
            dest_dir_c = values['folder_c']
            compress_files(compress_path, dest_dir_c)
            window['output_c'].update(value='Compression completed!')
            window['input1_e'].update(value='')
            window['input2_e'].update(value='')

        case sg.WIN_CLOSED:
            break

window.close()