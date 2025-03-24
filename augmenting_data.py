import librosa
import os
import numpy as np
import soundfile as sf

# Tăng tốc độ
def increase_speed(y, sr):
    """
    :param y: Tín hiệu âm thanh đầu vào.
    :param rate: Tỷ lệ thay đổi tốc độ (ví dụ: 1.1 để tăng tốc độ lên 10%).
    :return: Tín hiệu âm thanh đã thay đổi tốc độ.
    """
    y = y.astype(float)
    # Chuyển tín hiệu âm thanh thành STFT
    #stft = librosa.stft(y)
    
    # Áp dụng time-stretch lên phổ STFT
    #stretched_stft = librosa.effects.time_stretch(stft.astype(float), rate=1.5)
    stretched_stft = librosa.effects.time_stretch(y, rate=1.5)
    
    # Chuyển lại phổ STFT thành tín hiệu âm thanh
    #return librosa.istft(stretched_stft)
    return stretched_stft

# Giảm tốc độ
def decrease_speed(y, sr):
    """
    :param y: Tín hiệu âm thanh đầu vào.
    :param rate: Tỷ lệ thay đổi tốc độ (ví dụ: 1.1 để tăng tốc độ lên 10%).
    :return: Tín hiệu âm thanh đã thay đổi tốc độ.
    """
    y = y.astype(float)
    # Chuyển tín hiệu âm thanh thành STFT
    #stft = librosa.stft(y)
    
    # Áp dụng time-stretch lên phổ STFT
    #stretched_stft = librosa.effects.time_stretch(stft.astype(float), rate=1.5)
    stretched_stft = librosa.effects.time_stretch(y, rate=0.75)
    
    # Chuyển lại phổ STFT thành tín hiệu âm thanh
    #return librosa.istft(stretched_stft)
    return stretched_stft

# Tăng cao độ
def increase_pitch(y, sr):
    """
    Thay đổi cao độ tín hiệu âm thanh.
    :param y: Tín hiệu âm thanh đầu vào.
    :param sr: Tần số mẫu (sampling rate).
    :param n_steps: Số bán âm (semitones) để thay đổi cao độ.
    :return: Tín hiệu âm thanh đã thay đổi cao độ.
    """
    return librosa.effects.pitch_shift(y=y, sr=sr, n_steps=4)

# Giảm cao độ
def decrease_pitch(y, sr):
    """
    Thay đổi cao độ tín hiệu âm thanh.
    :param y: Tín hiệu âm thanh đầu vào.
    :param sr: Tần số mẫu (sampling rate).
    :param n_steps: Số bán âm (semitones) để thay đổi cao độ.
    :return: Tín hiệu âm thanh đã thay đổi cao độ.
    """
    return librosa.effects.pitch_shift(y=y, sr=sr, n_steps=-4)

# Thêm nhiễu nền (Add Noise)
def add_noise(y, sr):
    """
    Thêm nhiễu ngẫu nhiên vào tín hiệu âm thanh.
    :param y: Tín hiệu âm thanh đầu vào.
    :param noise_level: Mức độ nhiễu cần thêm vào.
    :return: Tín hiệu âm thanh với nhiễu.
    """
    noise_level=0.05
    return y + noise_level * np.random.randn(len(y))

# Hàm tăng cường và lưu file
def augment_audio(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for label in os.listdir(output_dir):
        label_path = os.path.join(output_dir, label)
        for file in os.listdir(label_path):
            file_path = os.path.join(label_path, file)
            if os.path.isfile(file_path):  # Check if it's a file
                os.remove(file_path)  # Delete file
    
    for label in os.listdir(input_dir):
        label_folder = os.path.join(input_dir, label)
        output_label_folder = os.path.join(output_dir, label)
        os.makedirs(output_label_folder, exist_ok=True)

        files = [f for f in os.listdir(label_folder) if f.endswith(".wav")]

        #if num_files >= target_count:
            #print(f"Label '{label}' đã có đủ file, bỏ qua tăng cường.")
            #continue

        print(f"Tăng cường dữ liệu cho '{label}'...")
        for file_name in files:
            file_path = os.path.join(label_folder, file_name)
            y, sr = librosa.load(file_path, sr=16000)
            y = y.astype(np.float32)

            sf.write(os.path.join(output_label_folder, file_name), y, sr)

            augment_functions = [increase_speed, decrease_speed, increase_pitch, decrease_pitch, add_noise]
            i = 0
            for func in augment_functions:
                #func = np.random.choice(augment_functions)
                augmented_audio = func(y, sr)
                augmented_file_name = f"{os.path.splitext(file_name)[0]}_aug_{i+1}.wav"
                augmented_file_path = os.path.join(output_label_folder, augmented_file_name)
                sf.write(augmented_file_path, augmented_audio, sr)
                i += 1

# Đường dẫn dữ liệu
input_directory = "d:\doAnTN\splited_data"  # Thư mục chứa dữ liệu gốc
output_directory = "d:\doAnTN\Augmented_data"  # Thư mục lưu dữ liệu tăng cường

# Gọi hàm tăng cường
augment_audio(input_directory + "\Train" , output_directory + "\Train")
augment_audio(input_directory + "\Validation" , output_directory + "\Validation")
augment_audio(input_directory + "\Test" , output_directory + "\Test")
